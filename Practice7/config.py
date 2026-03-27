# Example 1: Store configuration settings
config = {"theme": "dark", "language": "en", "autosave": True}
print("Config settings:", config)

# Example 2: Update a setting
config["language"] = "fr"
print("Updated config:", config)

# Example 3: Check a setting
if config.get("autosave"):
    print("Autosave is enabled")
else:
    print("Autosave is disabled")