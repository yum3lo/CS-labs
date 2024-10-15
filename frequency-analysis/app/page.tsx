"use client";
import React, { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { ScrollArea } from "@/components/ui/scroll-area";

interface FrequencyData {
  letter: string;
  frequency: number;
}

const englishFrequency: FrequencyData[] = [
  { letter: "A", frequency: 7.9 },
  { letter: "B", frequency: 1.4 },
  { letter: "C", frequency: 2.7 },
  { letter: "D", frequency: 4.1 },
  { letter: "E", frequency: 12.2 },
  { letter: "F", frequency: 2.1 },
  { letter: "G", frequency: 1.9 },
  { letter: "H", frequency: 5.9 },
  { letter: "I", frequency: 6.8 },
  { letter: "J", frequency: 0.2 },
  { letter: "K", frequency: 0.8 },
  { letter: "L", frequency: 3.9 },
  { letter: "M", frequency: 2.3 },
  { letter: "N", frequency: 6.5 },
  { letter: "O", frequency: 7.2 },
  { letter: "P", frequency: 1.8 },
  { letter: "Q", frequency: 0.1 },
  { letter: "R", frequency: 5.8 },
  { letter: "S", frequency: 6.1 },
  { letter: "T", frequency: 8.8 },
  { letter: "U", frequency: 2.7 },
  { letter: "V", frequency: 1.0 },
  { letter: "W", frequency: 2.3 },
  { letter: "X", frequency: 0.2 },
  { letter: "Y", frequency: 1.9 },
  { letter: "Z", frequency: 1.0 },
];

const FrequencyAnalysisDecryption: React.FC = () => {
  const [encryptedText, setEncryptedText] = useState<string>("");
  const [frequencyData, setFrequencyData] = useState<FrequencyData[]>([]);
  const [substitutionMap, setSubstitutionMap] = useState<
    Record<string, string>
  >({});
  const [decryptedText, setDecryptedText] = useState<string>("");

  const analyzeFrequency = (): void => {
    const frequency: Record<string, number> = {};
    const totalChars = encryptedText.length;

    for (const char of encryptedText.toUpperCase()) {
      if (/[A-Z]/.test(char)) {
        frequency[char] = (frequency[char] || 0) + 1;
      }
    }

    const data: FrequencyData[] = Object.entries(frequency)
      .map(([letter, count]) => ({
        letter,
        frequency: Number(((count / totalChars) * 100).toFixed(1)),
      }))
      .sort((a, b) => a.letter.localeCompare(b.letter));

    setFrequencyData(data);
  };

  const handleSubstitution = (
    encryptedChar: string,
    decryptedChar: string
  ): void => {
    setSubstitutionMap((prev) => ({
      ...prev,
      [encryptedChar]: decryptedChar,
    }));
  };

  const decryptText = (): void => {
    let decrypted = "";
    for (const char of encryptedText.toUpperCase()) {
      if (/[A-Z]/.test(char)) {
        decrypted += substitutionMap[char] || "*";
      } else {
        decrypted += char;
      }
    }
    setDecryptedText(decrypted);
  };

  return (
    <div className="p-12 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">
        Frequency Analysis and Decryption Project
      </h1>

      <h2 className="text-xl font-semibold mb-4">English Letter Frequency</h2>
      <ResponsiveContainer width="100%" height={200}>
        <BarChart data={englishFrequency}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="letter" />
          <YAxis />
          <Tooltip />
          <Bar
            dataKey="frequency"
            fill="hsl(var(--dark-pink))"
            radius={[5, 5, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>

      <h2 className="text-xl font-semibold mt-6 mb-4">Encrypted Text</h2>
      <Textarea
        value={encryptedText}
        onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) =>
          setEncryptedText(e.target.value)
        }
        placeholder="Enter the encrypted text here..."
        className="w-full min-h-[230px] mb-4 border-border border-2 focus:border-ring bg-card p-4"
      />
      <Button onClick={analyzeFrequency}>Analyze Frequency</Button>

      {frequencyData.length > 0 && (
        <>
          <h2 className="text-xl font-semibold mt-6 mb-4">
            Encrypted Text Frequency
          </h2>
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={frequencyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="letter" />
              <YAxis />
              <Tooltip />
              <Bar
                dataKey="frequency"
                fill="hsl(var(--dark-green))"
                radius={[5, 5, 0, 0]}
              />
            </BarChart>
          </ResponsiveContainer>

          <h2 className="text-xl font-semibold mt-6 mb-2">Substitution</h2>
          <div className="grid grid-cols-6 gap-2 mb-4">
            {frequencyData.map(({ letter }) => (
              <div key={letter} className="flex items-center">
                <span className="mr-2">{letter}:</span>
                <Input
                  value={substitutionMap[letter] || ""}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    handleSubstitution(letter, e.target.value.toUpperCase())
                  }
                  maxLength={1}
                  className="w-10 border-border border-2 focus:border-ring bg-card"
                />
              </div>
            ))}
          </div>
          <Button onClick={decryptText} className="mb-4">
            Decrypt Text
          </Button>

          {decryptedText && (
            <>
              <h2 className="text-xl font-semibold mb-2">Decrypted Text</h2>
              <ScrollArea className="h-[230px] w-[900px] rounded-md border-border border-2 focus:border-ring bg-card p-4">
                {decryptedText}
              </ScrollArea>
            </>
          )}
        </>
      )}
    </div>
  );
};

export default FrequencyAnalysisDecryption;
