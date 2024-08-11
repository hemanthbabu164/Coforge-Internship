import React from "react";
import { Button } from "@mui/material";

function UploadSection({ file, setFile, handleUpload }) {
  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <Button variant="contained" onClick={handleUpload}>
        Upload
      </Button>
      <Button variant="outlined" onClick={() => setFile(null)}>
        Cancel
      </Button>
    </div>
  );
}

export default UploadSection;
