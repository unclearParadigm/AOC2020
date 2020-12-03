using System;
using System.IO;
using System.Linq;

namespace AOC2020_02 {
    internal static class Program {
        private class PolicyEntry {
            public int Min { get; set; }
            public int Max { get; set; }
            public char Char { get; set; }
            public string Password { get; set; }

            public static PolicyEntry CreateFrom(string line) {
                var split = line.Split(':');
                return new PolicyEntry {
                    Char = split[0].Split(' ')[1][0],
                    Password = split[1].Trim(),
                    Max = Convert.ToInt32(split[0].Split(' ')[0].Split('-')[1]),
                    Min = Convert.ToInt32(split[0].Split(' ')[0].Split('-')[0])
                };
            }
           
            public bool IsValidPasswordAccordingToPart1Policies() {
                var occurenceCount = Password.Count(c => c == Char);
                return occurenceCount >= Min && occurenceCount <= Max;
            }
           
            public bool IsValidPasswordAccordingToPart2Policies() {
                var c1 = Password[Min - 1];
                var c2 = Password[Max - 1];
                return (c1 == Char || c2 == Char) && c1 != c2;
            }
        }

        private static void Main(string[] args) {
            var policies = File.ReadAllLines("./aoc2020_02_input.txt")
                .Where(l => !string.IsNullOrWhiteSpace(l))
                .Select(PolicyEntry.CreateFrom)
                .ToList();
           
            Console.WriteLine($"Part 1: {policies.Count(p => p.IsValidPasswordAccordingToPart1Policies())}");
            Console.WriteLine($"Part 2: {policies.Count(p => p.IsValidPasswordAccordingToPart2Policies())}");
        }
    }
}
