using System.Net.Sockets;
using System.Text;
using System.Text.Json;

Console.WriteLine("Device Simulator Started");

try
{
while (true)
{
    Random random = new();
	        string[] devices =
{
    "DEV001",
    "DEV002",
    "DEV003"
};
    var reading = new DeviceReading
    {

	DeviceId =
    devices[random.Next(devices.Length)],
        Temperature = Math.Round(
            (decimal)(20 + random.NextDouble()*15),2),
        Humidity = Math.Round(
            (decimal)(40 + random.NextDouble()*50),2),
        Timestamp = DateTime.Now
    };

    string message =
        JsonSerializer.Serialize(reading);

    using TcpClient client = new();

    await client.ConnectAsync(
        "127.0.0.1",
        5000);

    Console.WriteLine(
        "Connected to server");

    using NetworkStream stream =
        client.GetStream();

    byte[] data =
        Encoding.UTF8.GetBytes(message);

    await stream.WriteAsync(data);

    Console.WriteLine(
        $"Sent: {message}");

    await Task.Delay(5000);
}
}
catch (Exception ex)
{
    Console.WriteLine(
        $"Error: {ex.Message}");
}

Console.WriteLine(
    "Press any key to exit");

Console.ReadKey();