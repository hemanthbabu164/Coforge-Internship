import React from "react";
import { TextField, Button, Box } from "@mui/material";

function SearchSection({ searchKeyword, setSearchKeyword, handleSearch }) {
  return (
    <Box marginTop={3}>
      <TextField
        label="Enter Keyword"
        variant="outlined"
        value={searchKeyword}
        onChange={(e) => setSearchKeyword(e.target.value)}
        fullWidth
      />
      <Button variant="contained" onClick={handleSearch} marginTop={10}>
        Search
      </Button>
    </Box>
  );
}

export default SearchSection;
