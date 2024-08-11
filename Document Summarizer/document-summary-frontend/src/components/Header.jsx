import React from "react";
import { AppBar, Toolbar, Typography, Box, Container } from "@mui/material";

function Header() {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        width: "100%",
      }}
    >
      <AppBar
        position="static"
        sx={{
          backgroundColor: "#1976d2",
          boxShadow: "0px 4px 8px rgba(0, 0, 0, 0.5)",
          width: "auto",
          borderRadius: "8px",
          margin: "16px 0",
        }}
      >
        <Toolbar sx={{ display: "flex", justifyContent: "center" }}>
          <Container
            maxWidth="md"
            sx={{ textAlign: "center", width: "auto", padding: "0" }}
          >
            <Typography variant="h2" component="h2">
              Document Summary Generator
            </Typography>
          </Container>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default Header;
