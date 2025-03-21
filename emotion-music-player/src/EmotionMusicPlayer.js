import React, { useState } from "react";

const EmotionMusicPlayer = () => {
  const [text, setText] = useState(""); // Eingabetext
  const [emotion, setEmotion] = useState(""); // Klassifizierte Emotion
  const [loading, setLoading] = useState(false); // Ladezustand

  // API-Aufruf für Emotionserkennung
  const classifyEmotion = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/classify", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setEmotion(data.emotion);
    } catch (error) {
      console.error("Fehler bei der Klassifikation:", error);
    } finally {
      setLoading(false);
    }
  };

  // Textfeld und Button
  return (
    <div>
      <h1>Emotion Music Player</h1>
      <textarea
        placeholder="Gib deinen Text hier ein..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={classifyEmotion} disabled={loading}>
        {loading ? "Lädt..." : "Emotion analysieren"}
      </button>
      {emotion && <p>Erkannte Emotion: {emotion}</p>}
    </div>
  );
};

export default EmotionMusicPlayer;
