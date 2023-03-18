from routeros_ssh_connector import MikrotikDevice

router = MikroTikDevice()
router.connect("ip_address", "username", "password", "port")
interfaces = router.get_interfaces()
print(interfaces)