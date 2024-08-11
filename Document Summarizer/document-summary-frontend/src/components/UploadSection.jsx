import React from "react";
import { Button } from "@mui/material";

function UploadSection({ file, setFile, handleUpload }) {
  return (
    <div className="uploadSection">
      <div className="fileInput">
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      </div>
      <div className="ucButtonSection">
        <Button variant="contained" onClick={handleUpload}>
          Upload
        </Button>
        <Button variant="outlined" onClick={() => setFile(null)}>
          Cancel
        </Button>
      </div>
    </div>
  );
}

export default UploadSection;
