import React, { useState } from "react";
import { checkSymptoms } from "./api";
import ReactMarkdown from "react-markdown";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await checkSymptoms(text);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      style={{
        minHeight: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#0e0e10",
        color: "#fff",
        fontFamily: "'Inter', sans-serif",
        padding: "1rem",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "700px",
          backgroundColor: "#16161a",
          borderRadius: "16px",
          padding: "2.5rem",
          boxShadow: "0 0 25px rgba(0, 0, 0, 0.5)",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: "1.5rem" }}>
          <img
            src="https://cdn-icons-png.flaticon.com/512/3774/3774299.png"
            alt="doctor icon"
            width="70"
            style={{ marginBottom: "1rem" }}
          />
          <h1 style={{ fontSize: "2rem", fontWeight: "700" }}>
            Healthcare Symptom Checker
          </h1>
        </div>

        {/* Form */}
        <form
          onSubmit={handleSubmit}
          style={{ width: "100%", textAlign: "center" }}
        >
          <textarea
            rows="5"
            placeholder="Describe your symptoms..."
            value={text}
            onChange={(e) => setText(e.target.value)}
            style={{
              width: "100%",
              padding: "1rem",
              borderRadius: "10px",
              backgroundColor: "#1c1c21",
              color: "#fff",
              fontSize: "1rem",
              border: "1px solid #2a2a30",
              marginBottom: "1rem",
              resize: "none",
              outline: "none",
            }}
          />
          <button
            type="submit"
            disabled={loading || !text.trim()}
            style={{
              backgroundColor: loading ? "#333" : "#007BFF",
              color: "white",
              fontWeight: "600",
              padding: "0.75rem 2rem",
              border: "none",
              borderRadius: "10px",
              cursor: "pointer",
              transition: "0.3s",
            }}
          >
            {loading ? "Checking..." : "Submit"}
          </button>
        </form>

        {/* Error Message */}
        {error && (
          <p
            style={{
              color: "tomato",
              marginTop: "1rem",
              fontWeight: "500",
              textAlign: "center",
            }}
          >
            {error}
          </p>
        )}

        {/* Results */}
        {result && (
          <div
            style={{
              backgroundColor: "#1c1c21",
              marginTop: "2rem",
              padding: "1.5rem",
              borderRadius: "10px",
              border: "1px solid #2a2a30",
              width: "100%",
              textAlign: "left",
            }}
          >
            <h2 style={{ fontSize: "1.25rem", marginBottom: "0.5rem" }}>
              Probable Conditions:
            </h2>
            <ReactMarkdown>{result.probable_conditions}</ReactMarkdown>

            <h2 style={{ fontSize: "1.25rem", marginTop: "1rem" }}>
              Recommendations:
            </h2>
            <ReactMarkdown>{result.recommendations}</ReactMarkdown>

            <h3
              style={{
                fontSize: "1.1rem",
                marginTop: "1rem",
                color: "#9f9",
              }}
            >
              Disclaimer:
            </h3>
            <ReactMarkdown>{result.disclaimer}</ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
}
