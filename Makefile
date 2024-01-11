# Remove Unpacked Artifacts
clean:
	rm -rf antminer_sd_fw

unpack: clean
	unzip ./Antminer-S19Pro-SD-202006012027-release.zip -d antminer_sd_fw
	dd bs=1 skip=64 if=antminer_sd_fw/update.image.gz of=antminer_sd_fw/update_no_header.image.gz
	gunzip antminer_sd_fw/update_no_header.image.gz
	sudo mkdir -p /mnt/antminer
	sudo mount -o loop antminer_sd_fw/update_no_header.image /mnt/antminer
	mkdir -p ./antminer_sd_fw/update_no_header
	sudo cp -r /mnt/antminer/* ./antminer_sd_fw/update_no_header
	sudo umount /mnt/antminer
