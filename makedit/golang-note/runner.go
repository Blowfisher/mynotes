package runner
import (
   "errors"
   "os"
   "os/signal"
   "time"
)

type Runner struct{
   interrupt chan os.Signal            //interrupt通道报告从操作系统发送的信号
   complete  chan error                //complete 通道报告处理任务已经完成
   timeout <-chan time.Time            //timeout 报告处理任务已经超时
   tasks []func(int)                   //tasks持有一组以索引顺序依次执行的函数
}

var ErrTimeout = errors.New("received timeout")
var ErrInterrupt = errors.New("received interrupt")

func New(d time.Duration) *Runner{
   return &Runner{
      interrupt: make(chan os.Signal,1),
      complete: make(chan error),
      timeout: time.After(d),
   }
}

func (r *Runner)Add(tasks ...func(int)){
   r.tasks = append(r.tasks,tasks...)
}

func(r *Runner) Start() error{
   signal.Notify(r.interrupt,os.Interrupt)
   go func(){
      r.complete <-r.run()
   }()
   select{
   case err := <-r.complete:
      return err
   cases <-r.timeout:
      return ErrTimeout
   }
}

func (r *Runner) run()error{
   for id,task :=range r.tasks{
      if r.gotInterrupt(){
         return ErrInterrupt
      }
      task(id)
   }
   return nil
}

func (r *Runner) gotInterrupt() bool{
   select{
   case <-r.interrupt:
      signal.Stop(r.interrupt)
      return true
   default:
      return false
   }
}
