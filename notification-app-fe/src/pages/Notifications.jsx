import { useEffect, useState } from "react";
import { api } from "./../../../notification-app-be/services";
import NotificationCard from "../components/NotificationCard";

import {
  Container,
  Typography,
} from "@mui/material";

export default function AllNotifications() {

  const [notifications, setNotifications] = useState([]);

  useEffect(() => {

    api.get("/notifications")
      .then((res) => {
        setNotifications(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

  }, []);

  return (
    <Container sx={{ mt: 4 }}>
        <Typography 
  variant="h4" 
  gutterBottom 
  sx={{ 
    color: '#ffffffff', 
    fontFamily: 'system-ui, sans-serif', 
    fontWeight: 'bold',
  }}
>
  All Notifications
</Typography>

      {notifications.map((item) => (
        <NotificationCard
          key={item.ID}
          notification={item}
        />
      ))}
    </Container>
  );
}