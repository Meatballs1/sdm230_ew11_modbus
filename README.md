# sdm230_ew11_modbus
Some steps for integrating Eastron SDM230 Electricity Meter into Home Assistant via the Elfin EW11 Wifi Modbus interface

SDM230 Modbus Documentation:

https://ozeki.hu/attachments/5849/Eastron_SDM230Modbus_modbus_protocol.pdf

EW11 Configuration:

![image](https://user-images.githubusercontent.com/1854557/217095469-df918b7a-420f-49f9-8af1-2251d47cfc74.png)

![image](https://user-images.githubusercontent.com/1854557/217095519-049a1b9b-1ca5-44bd-997c-d040be79b23a.png)

Home Assistant Modbus Settings:

```
modbus:
  - type: tcp
    name: "ew11"
    host: ew11.local
    port: 502
    close_comm_on_error: true
    timeout: 9
    retry_on_empty: true
    retries: 10
    sensors:
      - name: "SDM230 Voltage"
        address: 0
        data_type: float32
        slave: 1
        unit_of_measurement: V
        input_type: input
        scale: 1
        precision: 1
        scan_interval: 10
        device_class: voltage
      - name: "SDM230 Active Power"
        address: 0xC
        data_type: float32
        slave: 1
        unit_of_measurement: W
        input_type: input
        scale: 1
        precision: 1
        scan_interval: 10
        device_class: power
      - name: "SDM230 Import Active Energy"
        address: 0x48
        data_type: float32
        slave: 1
        unit_of_measurement: kWh
        input_type: input
        scale: 1
        precision: 2
        scan_interval: 10
        device_class: energy
        state_class: measurement
      - name: "SDM230 Export Active Energy"
        address: 0x4A
        data_type: float32
        slave: 1
        unit_of_measurement: kWh
        input_type: input
        scale: 1
        precision: 2
        scan_interval: 10
        device_class: energy
        state_class: measurement
```

Wiring:

I just used 2 core cable to connect A to A and B to B - I didn't need any line resistors or to connect a common ground, but the cable wasn't that long.
