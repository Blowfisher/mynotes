ackage main

import "fmt"

//import t "time"

type mom int

type user struct {
	name string
	email string
	age int
}

func (u user) fnm(){
	fmt.Println("name: ",u.name,"email: ",u.email)
}

func fn(a []int)[]int{
   a[0]=12
   return a
}

func main() {
	//	t.Sleep(t.Second)
	slice := []int{10, 20, 30, 40, 50}
	newSlice := slice[2:3:4]
	fmt.Println("slice: ", slice, "newslice: ", newSlice)
	fmt.Println("len: ", len(newSlice), "cap: ", cap(newSlice))
	for index,value := range slice {
		fmt.Println("index: ",index,"value: ",value)
	}
	b := fn(slice)
	fmt.Println("b: ",b,"slice: ",slice)
	var name mom
	name = 1
	fmt.Println("name ",name)
	man := user{"kiki","22333@qq.com",18}
	man.fnm()
}
