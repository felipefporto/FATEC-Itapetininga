using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aula_2023_02_23_Exer_2
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 0, b = 0, total = 0;

            Console.Write("Informe o um valor:");
            a = int.Parse(Console.ReadLine());
            Console.Write("Informe o segundo valor:");
            b = int.Parse(Console.ReadLine());

            total = a + b;

            Console.Write($"O total é: {total}");
            Console.ReadLine();

        }
    }
}
