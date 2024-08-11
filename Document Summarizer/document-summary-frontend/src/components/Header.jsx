import React from "react";
import { AppBar, Toolbar, Typography, Container } from "@mui/material";

function Header() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Container>
          <Typography variant="h2" component="div">
            Document Summary Generator
          </Typography>
        </Container>
      </Toolbar>
    </AppBar>
  );
}
export default Header;
