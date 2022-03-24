using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _1
{
    public class LogicOperations
    {
        public bool a;
        public bool b;

        public bool AND(bool a, bool b)
        {
            return (bool)a && b;
        }

        public bool OR(bool a, bool b)
        {
            return (bool)a || b;
        }
    }
}
