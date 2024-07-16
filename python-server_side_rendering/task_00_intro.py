import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        processed_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace(f"{{{{ {key} }}}}", value)

        # Generate output file
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
        print(f"Generated {output_filename}")
