import re

# Predefined knowledge base from documentation (sample)
documentation = {
    'segment': {
        'setup_source': "To set up a new source in Segment, go to your Segment workspace, select 'Sources', and click 'Add Source'. Follow the on-screen instructions to complete the setup.",
        'create_user_profile': "To create a user profile in Segment, go to the 'Profiles' section and click 'Add Profile'. Fill in the required fields like email and user attributes.",
        'create_audience_segment': "To create an audience segment in Segment, go to the 'Audiences' section and click 'Create Audience'. Choose attributes like user behavior and demographics.",
        'integrate_data': "To integrate data with Segment, go to the 'Destinations' section, select 'Add Destination', and choose the desired destination for your data."
    },
    'mparticle': {
        'setup_source': "To set up a new source in mParticle, go to the 'Integrations' section, select 'Add Source', and follow the setup process.",
        'create_user_profile': "To create a user profile in mParticle, navigate to the 'Users' section, and click 'Create New User Profile'. Add all necessary details such as email, user ID, and other attributes.",
        'create_audience_segment': "To create an audience segment in mParticle, go to the 'Audiences' section and click 'Create Segment'. Use filters like events and attributes to define your segment.",
        'integrate_data': "To integrate data with mParticle, go to the 'Integrations' tab, select 'Add Integration', and follow the setup instructions for your data destination."
    },
    'lytics': {
        'setup_source': "To add a source in Lytics, go to the 'Sources' section from your Lytics dashboard and select 'Add Source'. Follow the wizard to integrate your source.",
        'create_user_profile': "In Lytics, user profiles are automatically created through data integrations. Ensure that your data flow includes profile information like user ID and email.",
        'create_audience_segment': "To create an audience segment in Lytics, navigate to the 'Segments' section and click 'Create Segment'. Define segments based on user behaviors and attributes.",
        'integrate_data': "To integrate data with Lytics, go to the 'Destinations' section and configure your data integration with external tools."
    },
    'zeotap': {
        'setup_source': "To set up a source in Zeotap, access the 'Data Sources' section in the platform and select 'Add New Source'. Follow the provided instructions.",
        'create_user_profile': "Zeotap provides customer profiles automatically once data is ingested through integrated sources.",
        'create_audience_segment': "To create an audience segment in Zeotap, go to the 'Audience Builder' and select 'Create Segment'. Choose from data sources like user demographics and behaviors.",
        'integrate_data': "To integrate data with Zeotap, go to the 'Integrations' section, choose 'Add Integration', and follow the instructions to link your data source."
    }
}

# Basic chatbot functionality
class CDPChatbot:
    def __init__(self, doc):
        self.doc = doc
    
    def handle_question(self, question):
        # Clean and preprocess the question
        question = question.lower()
        
        # Check for common question patterns and match to documentation
        if "how do i set up a new source" in question:
            return self.get_answer('setup_source')
        
        elif "create a user profile" in question:
            return self.get_answer('create_user_profile')
        
        elif "create an audience segment" in question:
            return self.get_answer('create_audience_segment')
        
        elif "integrate my data" in question or "how can i integrate my data" in question:
            return self.get_answer('integrate_data')
        
        elif "how does segment's audience creation" in question:
            return self.cross_cdp_comparison('segment', 'lytics')
        
        elif "how does mparticle's audience creation" in question:
            return self.cross_cdp_comparison('mparticle', 'zeotap')
        
        else:
            return "Sorry, I didn't understand the question. Could you please rephrase?"

    def get_answer(self, task):
        for cdp, tasks in self.doc.items():
            if task in tasks:
                return tasks[task]
        return "Sorry, I don't have information on that task."

    def cross_cdp_comparison(self, cdp1, cdp2):
        # Return a cross-CDP comparison for audience creation (or any other feature)
        comparison_map = {
            'segment': 'Segment uses demographic, behavioral, and event-based attributes to define audiences.',
            'mparticle': 'mParticle creates audiences using event data and user attributes.',
            'lytics': 'Lytics is known for behavioral analysis and segmenting based on past actions.',
            'zeotap': 'Zeotap leverages first-party data and advanced analytics for audience segmentation.'
        }
        comparison_1 = comparison_map.get(cdp1, "No information available.")
        comparison_2 = comparison_map.get(cdp2, "No information available.")
        
        return f"{cdp1.capitalize()} Audience Creation: {comparison_1}\n{cdp2.capitalize()} Audience Creation: {comparison_2}"

# Initialize chatbot
chatbot = CDPChatbot(documentation)

# Sample interaction
def chatbot_interaction():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.handle_question(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot_interaction()

