import {
  Card,
  CardContent,
  Typography,
  Chip,
} from "@mui/material";

export default function NotificationCard({ notification }) {
  return (
    <Card sx={{ mb: 2 }}>
      <CardContent>
        <Chip
          label={notification.Type}
          color="primary"
          sx={{ mb: 1 }}
        />

        <Typography variant="h6">
          {notification.Message}
        </Typography>

        <Typography color="text.secondary">
          {notification.Timestamp}
        </Typography>
      </CardContent>
    </Card>
  );
}

