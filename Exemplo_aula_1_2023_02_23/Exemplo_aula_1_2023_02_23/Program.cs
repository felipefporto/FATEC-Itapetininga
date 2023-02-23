using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exemplo_aula_1_2023_02_23
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Hello World!\n");

            int a, b, total;
            a = 20;
            b = 10;

            Console.WriteLine(a + " + " + b + " = " + (a + b));
            total = a - b;
            Console.WriteLine(a + "-" + b + "=" + total);
            Console.WriteLine(a + "*" + b + "=" + (a * b));
            Console.WriteLine(a + " / " + b + " = " + (a / b));
            Console.WriteLine(a + "%" + b + "=" + (a % b));

            Console.ReadKey();

        }
    }
}
