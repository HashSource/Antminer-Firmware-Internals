## Unpack SD Firmware

- `make unpack`

## Useful Directories

- `antminer_sd_fw/update_no_header`
- `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header`

## GPIO

- GPIO 907 -> PSU
- GPIO 941 -> RED LED
- GPIO 942 -> GREEN LED

## Important Files

### SD Firmware

When the SD firmware boots, the `Update.sh` script is ran, and later the `FileParser` binary validates and unpacks `bin/update.bmu` using the `bitmain.pub` Bitmain public key. The unpacked files are written to NAND.

- `antminer_sd_fw/update_no_header/etc/init.d/S37bitmainer_setup`
- `antminer_sd_fw/update_no_header/etc/init.d/Update.sh`
- `antminer_sd_fw/update_no_header/etc/bitmain.pub`
- `antminer_sd_fw/update_no_header/usr/bin/FileParser`
- `antminer_sd_fw/bin/update.bmu`

To understand what `update.bmu` file looks like internally, we refer to the `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header` directory.

- `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header/etc/init.d/S70cgminer`

The `S70cgminer` script, loads the following linux drivers:

- `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header/lib/modules/fpga_mem_driver.ko`
- `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header/lib/modules/bitmain_axi.ko`

It's not clear yet, what the role of the drivers are.

Once the drivers are loaded, the following binaries are executed:

- `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header/usr/bin/cgminer`
- `Antminer_S19_Pro_zynq7007_BHB42XXX/minerfs_no_header/usr/bin/bmminer`

When `bmminer` is executed, it opens a socket on a specific port, waiting for a connection.
Once `cgminer` is also executed, it connects to `bmminer` via the open socket.

The role of `bmminer` is to initialize all hardware, Power Supply, Fans, And the three hashboards (motherboards) that are responsible for hashing.

Once the hardware is initialized, a `init` signal is sent to `cgminer`, and it begins connection the the user defined pools, and starts hashing (sending shares)
