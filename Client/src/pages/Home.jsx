import { useState } from "react";

const Home = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeText = async () => {
    if (!text.trim()) {
      setError("Please enter a text.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Error analyzing text. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-blue-900 p-4">
      <h1 className="text-2xl font-bold mb-4">DisasterGuard</h1>
      <textarea
        className="w-full max-w-lg p-2 border rounded-md shadow-sm bg-gray-300"
        rows="4"
        placeholder="Enter text regarding a disaster..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      ></textarea>
      <button
        onClick={analyzeText}
        className="mt-3 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition"
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {error && <p className="text-red-600 mt-2">{error}</p>}

      {result && (
        <div className="mt-4 p-4 rounded-md shadow-md w-full max-w-lg bg-gray-300">
          <h2 className="text-lg font-semibold">Analysis Result:</h2>
          <p><strong>Distress Level:</strong> {result.distress_level}</p>
        </div>
      )}
    </div>
  );
};

export default Home;
