# These and other macros are documented in dhd/droid-hal-device.inc.
# device is the cyanogenmod codename for the device
# eg mako is Nexus 4
%define device i9100g
# vendor is used in device/samsung/i9100g/
%define vendor samsung
# Manufacturer and device name to be shown in UI
%define vendor_pretty Samsung
%define device_pretty Galaxy S2 G

%define installable_zip 1

%include rpm/dhd/droid-hal-device.inc
