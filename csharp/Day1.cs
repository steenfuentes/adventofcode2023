using System;
using System.IO;

class Day1
{
    static void Main(string[] args)
    {
        using (StreamReader sr = File.OpenText("input.txt"))
        {
            string line;
            int total = 0;
            while ((line = sr.ReadLine()) != null)
            {
                total += CalibrateLine(line);
            }
            Console.WriteLine(total);
        }
        return;
    }

    public static char[]  LineDigits(string line)
    {
        char[] lineDigits = new char[2];
        foreach (char c in line)
        {
            if (Int32.TryParse(c.ToString(), out int digit))
            {
                if (lineDigits[0] == 0)
                {
                    lineDigits[0] = c;
                }
                else
                {
                    lineDigits[1] = c;
                }
                lineDigits.Append(c);
            }
        }
        return lineDigits;
    }

    public static int CalibrateLine(string line)
    {
        char[] lineDigits = LineDigits(line);
        int value;
        if (lineDigits[1] == 0)
        {
            return Int32.Parse(
                                lineDigits[0].ToString() +
                                lineDigits[0].ToString());
        }
        else
        {
            return Int32.Parse(
                                lineDigits[0].ToString() +
                                lineDigits[1].ToString());
        }
    }

}