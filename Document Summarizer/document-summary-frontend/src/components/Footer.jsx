import React from "react";
import { Typography, Box, Container } from "@mui/material";

function Footer() {
  return (
    <Box
      component="footer"
      padding={2}
      mt={4}
      bgcolor="#f5f5f5"
      textAlign="center"
    >
      <Container>
        <Typography variant="body2" color="textSecondary">
          &copy; {new Date().getFullYear()} Document Summary Generator.
        </Typography>
      </Container>
    </Box>
  );
}

export default Footer;
