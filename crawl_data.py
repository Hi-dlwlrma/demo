import logging
import sys
import os
from younet.crawler.solr.solr_query import to_solr_date_range
from younet.crawler.solr.mention import crawl_mentions


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)



# topic = '74059' #1
# topic = '74184' #2
topic = "72685"

fields = ('_version_', 'assign_status', 'attachment', 'category', 'comments', 'confident_score', 'copied_at',
          'created_date', 'date_gmt7', 'domain', 'engagement_date', 'engagement_s_c', 'engagement_total', 'id',
          'id_parent_comment', 'id_reference', 'id_source', 'id_table', 'identity', 'identity_birthday_year',
          'identity_city', 'identity_education_level', 'identity_gender', 'identity_job_level', 'identity_name',
          'is_approved', 'is_noisy', 'is_relevance', 'last_activity', 'last_sentiment', 'likes', 'link', 'link_shared',
          'man_updated_at', 'mention_type', 'negative_level', 'platform', 'search_text', 'sentiment', 'sentiment_auto',
          'shares', 'source_name', 'source_type', 'tags', 'title', 'topic_id', 'updated_at', 'views', 'is_ignore',
          'is_sample')


start_day, start_mon = 20, 6
end_day, end_mon = 21, 6
path = './data'

# while start_day < end_day:
FROM_DATE = (2022, start_mon, start_day)
TO_DATE = (2022, end_mon, end_day)
filters = {
    'fq': f'created_date:{to_solr_date_range(FROM_DATE, TO_DATE)}'
}

df = crawl_mentions(topic, fields, filters)

file_name = 'data' + ('%02d' % start_mon) + ('%02d' % start_day) + '_2.csv'
df.to_csv(os.path.join(path, file_name))

    # start_day += 1
