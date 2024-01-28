static void StackSort(Stack<int> s1)
        {
            Stack<int> s2 = new Stack<int>();
            Stack<int> s3 = new Stack<int>();
            while(!s1.IsEmpty())
            {
                while (!s2.IsEmpty() && s1.Top() > s2.Top())
                    s3.Push(s2.Pop());
                s2.Push(s1.Pop());
                while (!s3.IsEmpty())
                    s2.Push(s3.Pop());
            }
            while (!s2.IsEmpty())
                s1.Push(s2.Pop());
        }

        //  8*{3-(5+6)*[7-{3+9}/9]*[9*(6-5)]}
        //  {()[{}][()]}
        //  {()[{}][()]{
        //  {()[{}][()]
        //  {()[{]}[()]}
        //  {()[{}][()]}
        //  {()[{}][()]}
        //  }()[{}][()]}
        //  }{}
        //  {[]
        //  
        static void Main(string[] args)
        {
            Stack<int> s1 = new Stack<int>();

            s1.Push(88);
            s1.Push(22);
            s1.Push(33);
            s1.Push(44);
           
            s1.Push(22);
            s1.Push(11);
            s1.Push(99);
            s1.Push(77);
            Console.WriteLine(s1.ToString());
            StackSort(s1);
            Console.WriteLine(s1.ToString());



            //Console.WriteLine(s1.ToString());
            //Console.WriteLine(s1.ToString());
            //Console.WriteLine(s1.ToString());
            //Console.WriteLine(s1.ToString());
            //Console.WriteLine(MyToString(s1));




            //while(s1.IsEmpty()==false)
            //    Console.WriteLine(s1.Pop());
            //Console.WriteLine(s1.Pop());



        }
    }
}
