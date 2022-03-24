using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            new Program().Run(); 
        }

        public void Run()
        {
            Nwd nwd = new Nwd();
            Nww nww = new Nww();
            Console.WriteLine(nwd.NWD(4,8));
            Console.WriteLine(nww.NWW(128, 96));
            LogicOperations lo = new LogicOperations();
            Console.WriteLine(lo.AND(true, false));
            Console.WriteLine(lo.OR(true, false));
        }
    }
}
