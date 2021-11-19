import Search from "./Search"
import Registration from "./Registration"
import Login from "./Login"


import { ThemeProvider, createTheme } from "@material-ui/core"

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";



function App() {
  const theme = createTheme({
    background: {
      default: "#e9eaed"
    },
    typography: {
      fontFamily: '\'Montserrat\''
    },
    palette: {
      mode: 'light',
      primary: {
        main: '#835AA2'
      },
      success: {
        main: '#2DD700'
      },
      secondary: {
        main: '#FDC250'
      }
    },
  });
  return (
      <ThemeProvider theme={theme}>
        <Search />
      </ThemeProvider>
  );
}

export default App;
