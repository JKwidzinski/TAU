using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _1
{
    public class Nwd
    {
		public int a;
		public int b;
		public int NWD(int a, int b)
		{
			a = Math.Abs(a);
			b = Math.Abs(b);

			if (a == 0 && b == 0)
				throw new ArgumentException();

			if (a == 0)
				return b;

			if (b == 0)
				return a;

			while (a != b)
			{
				if (a > b)
					a -= b;
				else
					b -= a;
			}
			return a;
		}
	}
}
