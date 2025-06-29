#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Set the default Django settings module for the 'll_project' project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')
    
    try:
        # Try to import Django's execute_from_command_line function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle the case where Django isn't installed or available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command line arguments using Django's management utility
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Entry point - calls main() when script is run directly
    main()