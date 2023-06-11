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

    print('Test starts now')

    def test_room_booking_submit(self):
        # Submit the booking form
        response = self.client.post(reverse('room_booking', args=[self.room.Id]), {
            'Check-in': '20/5/2023',
            'Check-out': '25/5/2023',
            'ADULT': 2,
            'Children': 2,
            'Name': 'John',
            'Surname': 'Doe',
            'Email': 'john@example.com',
            'Phone Number': '456789',
            'City': 'New York',
            'Country': 'USA',
            'NID No': '123456789',
            'Address': '123 Main St',
        })

        print(response)

        # Ensure the booking is saved and success page is rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')
        self.assertTrue(Online_Booking.objects.filter(room=self.room).exists())
