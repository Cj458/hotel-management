from django.test import TestCase, Client
from django.urls import reverse
from .models import Add_Room, Online_Booking

# Remove the Room_Image when running tests.
class RoomBookingTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.room = Add_Room.objects.create(Id=1, Room_Type='Room 1')

    def test_room_booking_available(self):
        # Ensure the booking form is rendered when the room is available
        response = self.client.get(reverse('room_booking', args=[self.room.Id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')
        self.assertEqual(response.context['room'], self.room)

    def test_room_booking_occupied(self):
        # Create an existing booking for the room
        booking = Online_Booking.objects.create(room=self.room, Phone_Number='9033845')

        # Ensure the occupied page is rendered when the room is occupied
        response = self.client.get(reverse('room_booking', args=[self.room.Id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'occupied.html')

    def test_room_booking_submit(self):
        # Submit the booking form
        response = self.client.post(reverse('room_booking', args=[self.room.Id]), {
            'Check_in': '2023.05.20',
            'Check_out': '2023.5.25',
            'ADULT': 2,
            'CHILDREN': 2,
            'Name': 'John',
            'Surname': 'Doe',
            'Email': 'john@example.com',
            'Phone_Number': '456789',
            'City': 'New York',
            'Country': 'USA',
            'Nid_No': '123456789',
            'Address': '123 Main St',
        })

        # Ensure the booking is saved and success page is rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')
        self.assertTrue(Online_Booking.objects.filter(room=self.room).exists())
