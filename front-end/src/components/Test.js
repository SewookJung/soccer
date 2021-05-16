import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Test = () => {
  const [result, setResult] = useState(null);
  const message = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/');
      const resResult = res.data;
      setResult(resResult);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    message();
  }, []);

  return <div>{result}</div>;
};

export default Test;
