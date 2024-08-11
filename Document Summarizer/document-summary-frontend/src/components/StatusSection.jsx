import React from "react";
import { Typography, CircularProgress } from "@mui/material";

function StatusSection({ status }) {
  return (
    <div>
      <Typography variant="h6" marginTop={2}>
        Status: {status}
      </Typography>
      {status === "Processing Your Document..." && <CircularProgress />}
    </div>
  );
}
export default StatusSection;
