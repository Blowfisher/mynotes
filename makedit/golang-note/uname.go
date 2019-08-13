package main
import "fmt"


type Person struct{
    name string
    sex byte
    age int
}

type Student struct{
    Person  
    id int
    addr string
}

func main(){
    var s1 Student = Student{Person{"tom",'m',18},1,"Hunan"}
    fmt.Println("s1 = ",s1)
    
    s2 := Student{Person{"tom",'m',18},1,"Hunan"}
    fmt.Printf("s2 = %+v\n",s2)

    s3 := Student{id:1,addr:"Hunan"}
    fmt.Printf("s3 = %+v\n",s3)

    s4 := Student{Person: Person{name:"tom",age:18},addr:"Hunan"}
    fmt.Printf("s4 = %+v\n",s4)
}
