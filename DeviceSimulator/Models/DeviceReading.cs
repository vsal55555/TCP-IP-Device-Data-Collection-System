public class DeviceReading
{
    public string DeviceId { get; set; } = "";
    public decimal Temperature { get; set; }
    public decimal Humidity { get; set; }
    public DateTime Timestamp { get; set; }
}