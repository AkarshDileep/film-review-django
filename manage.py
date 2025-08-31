#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#!/usr/bin/env python
#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dbproj.settings")  # Replace with your actual project name

    # Only append host/port if "runserver" is already in the arguments and no port is defined
    if "runserver" in sys.argv and not any(":" in arg for arg in sys.argv):
        port = os.environ.get("PORT", "8000")
        sys.argv[sys.argv.index("runserver") + 1:] = [f"0.0.0.0:{port}"]

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()



# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbproj.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
