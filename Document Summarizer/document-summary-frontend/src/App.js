import React from "react";
import { Box } from "@mui/material";
import Header from "./components/Header";
import Main from "./components/Main";
import Footer from "./components/Footer";
import "./app.css";

function App() {
  return (
    <Box display="flex" flexDirection="column" minHeight="100vh">
      <Header />
      <Box
        component="main"
        flex="1" // This will make the Main component grow to fill available space
      >
        <Main />
      </Box>
      <Footer />
    </Box>
  );
}

export default App;
