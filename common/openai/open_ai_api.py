import os
from openai import OpenAI
from textwrap import wrap

class OpenAIAPI:
    def __init__(self, api_key=None):
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []

    def get_initial_message_text(self, channel_name):
        return (
            f"You will generate increasingly concise, entity-dense summaries "
            f"of the below Youtube video transcript from the channel {channel_name}. \n\n"
            "Repeat the following 2 steps 5 times. \n\n"
            "Step 1. Identify 1-5 informative entities (\";\" delimited) from the article "
            "which are missing from the previously generated summary. \n"
            "Step 2. Write a new, denser summary of identical length which covers every entity "
            "and detail from the previous summary plus the missing entities. \n\n"
            "A missing entity is:\n"
            "- relevant to the main story, \n"
            "- specific yet concise (5 words or fewer), \n"
            "- novel (not in the previous summary), \n"
            "- faithful (present in the transcript), \n"
            "- anywhere (can be located anywhere in the transcript).\n\n"
            "Guidelines:\n\n"
            "- The first summary should be long (11-21 sentences, ~1500 words) "
            "yet highly non-specific, containing little information beyond the entities marked as missing. "
            "Use overly verbose language and fillers (e.g., \"this video discusses\") to reach ~1337 words.\n"
            "- Make every word count: rewrite the previous summary to improve flow and make space for additional entities.\n"
            "- Don't repeat \"They\" often, make use of other phrases such as \"the team\", \"the guys\", etc. "
            "Use the channel name as reference more often.  Review for too many occurrences of any word.\n"
            "- Make space with fusion, compression, and removal of uninformative phrases like \"the video discusses\".\n"
            "- Phrases like \"This video discusses\" should be replaced with the name of the channel.\n"
            "- The summaries should become highly dense and concise yet self-contained, "
            "i.e., easily understood without the article. \n"
            "- Missing entities can appear anywhere in the new summary.\n"
            "- Never drop entities from the previous summary. If space cannot be made, add fewer new entities. \n"
            "- Write from the perspective of a fan of the Youtube channel that this transcript is from."
        )

    def get_summary_message_text(self, keywords):
        return (
            f"As a third-party, please re-summarize in 3-5 paragraphs by writing in the style of Jeremy Clarkson. "
            f"Don't repeat the phrase twice."
        )

    def get_short_summary_message_text(self):
        return (
            "Create an SEO optimized and user-friendly short summary for this blog article. "
            "Return nothing but the summary. The result should be 300 characters or less."
        )

    def get_blog_title_message_text(self):
        return (
            "Create an SEO optimized and user-friendly title for this blog article. "
            "Return nothing but the title. The result should be 70 characters or less."
        )

    def get_comment_message_text(self):
        return (
            "Please summarize the following comments for this video. "
            "Point out anything that might be of interest that you would have to watch the video to know. "
            "Create a list of the top ten commented topics as bullet points, don't mention users directly. "
            "Return only bullet points:\n"
        )

    def summarize_text_chat_completion(self, format, channel_name, text):
        if len(self.conversation_history) == 0 and format == "video_summary":
            self.conversation_history = [
                {"role": "system", "content": self.get_initial_message_text(channel_name)}
            ]
        elif len(self.conversation_history) == 0 and format == "comment_summary":
            self.conversation_history = [
                {"role": "system", "content": self.get_comment_message_text()}
            ]
        
        self.conversation_history.append({"role": "user", "content": text})

        try:
            response = self.client.chat.completions.create(
                # model="gpt-4o-mini",
                model="gpt-3.5-turbo-0125",
                messages=self.conversation_history,
                temperature=0.43,
                max_tokens=2901,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                timeout=120
            )

            if response.choices:
                new_message = response.choices[0].message
                self.conversation_history.append(new_message)
                print('conversation_history LENGTH END:', len(self.conversation_history))
                return new_message.content.strip()
            else:
                raise Exception("No choices returned by the API.")
        except Exception as e:
            raise Exception(f"OpenAI API error: {e}")

    def summarize_text_video_summary(self, transcript, channel_name, keywords):
        self.conversation_history = []  # reset conversation_history for every video
        initial_summary = self.summarize_text_chat_completion('video_summary', channel_name, transcript)
        summary_video = self.summarize_text_chat_completion('video_summary', channel_name, self.get_summary_message_text(keywords))
        short_summary = self.summarize_text_chat_completion('video_summary', channel_name, self.get_short_summary_message_text()).strip('\"')
        blog_title = self.summarize_text_chat_completion('video_summary', channel_name, self.get_blog_title_message_text()).strip('\"')
        return summary_video, short_summary, blog_title

    def summarize_text_comments(self, text, channel_name):
        self.conversation_history = []  # reset conversation_history for every video
        return self.summarize_text_chat_completion('comment_summary', channel_name, text)
