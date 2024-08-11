import React, { useState } from "react";
import UploadSection from "./UploadSection";
import StatusSection from "./StatusSection";
import SearchSection from "./SearchSection";
import SummarySection from "./SummarySection";
import { Box } from "@mui/material";
import axios from "axios";

function Main() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("No File Uploaded.");
  const [searchKeyword, setSearchKeyword] = useState("");
  const [summary, setSummary] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please Choose a File First.");
      return;
    }
    setStatus("Processing Your Document...");
    const formData = new FormData();
    formData.append("file", file);
    try {
      const uploadResponse = await axios.post(
        "http://localhost:8000/api/upload/",
        formData
      );
      console.log("Upload Response:", uploadResponse);
      setStatus(uploadResponse.data.message);
      const preprocessResponse = await axios.post(
        "http://localhost:8000/api/preprocess/"
      );
      setStatus(preprocessResponse.data.message);
    } catch (error) {
      const errorMessage =
        error.response?.data?.error || "Error Uploading or Preprocessing File.";
      setStatus(errorMessage);
    }
  };

  const handleSearch = async () => {
    if (!searchKeyword) {
      alert("Enter a Keyword First.");
      setSummary("Your Summary Will Be Diplayed Here.");
      return;
    }
    try {
      const response = await axios.get(
        `http://localhost:8000/api/summary/?keyword=${searchKeyword}`
      );
      console.log(response);
      setSummary(response.data.summary);
    } catch (error) {
      const errorMessage =
        error.response?.data?.error || "Error Fectching Summary.";

      setSummary(errorMessage);
    }
  };

  return (
    <Box padding={3}>
      <UploadSection
        file={file}
        setFile={setFile}
        handleUpload={handleUpload}
      />
      <StatusSection status={status} />
      <SearchSection
        searchKeyword={searchKeyword}
        setSearchKeyword={setSearchKeyword}
        handleSearch={handleSearch}
      />
      <SummarySection summary={summary} />
    </Box>
  );
}

export default Main;
