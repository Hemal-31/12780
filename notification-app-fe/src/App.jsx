import {
  BrowserRouter,
  Routes,
  Route,
  Link,
} from "react-router-dom";

import {
  AppBar,
  Toolbar,
  Button,
} from "@mui/material";

import Notifications from "./pages/Notifications";
import PriorityNotifications from "./pages/PriorityNotifications";
import "./App.css";
function App() {

  return (
    <BrowserRouter>

      <AppBar position="static">
        <Toolbar>

          <Button
            color="inherit"
            component={Link}
            to="/"
          >
            All Notifications
          </Button>

          <Button
            color="inherit"
            component={Link}
            to="/priority"
          >
            Priority Notifications
          </Button>

        </Toolbar>
      </AppBar>

      <Routes>

        <Route
          path="/"
          element={<Notifications />}
        />

        <Route
          path="/priority"
          element={<PriorityNotifications />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;