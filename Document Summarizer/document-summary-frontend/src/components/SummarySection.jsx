import React from "react";
import { Typography, Box } from "@mui/material";

function SummarySection({ summary }) {
  return (
    <Box className="summarySection" marginTop={3}>
      <Typography variant="h5" gutterBottom>
        Summary
      </Typography>
      <Typography variant="body1">
        {summary ? summary : "No Summary Available for the given Keyword."}
      </Typography>
    </Box>
  );
}
export default SummarySection;
