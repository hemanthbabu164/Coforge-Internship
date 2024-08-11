import React from "react";
import { Typography, Box } from "@mui/material";

function SummarySection({ summary }) {
  return (
    <Box marginTop={3}>
      <Typography variant="h5" gutterBottom>
        Summary
      </Typography>
      <Typography variant="body1">
        {summary ? summary : "No Summary Avilable for the given Keyword."}
      </Typography>
    </Box>
  );
}
export default SummarySection;
