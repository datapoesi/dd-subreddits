import styles from '../styles/misc.module.css'

export default function What() {
    return <div>
        <div className={styles.section}>
            <blockquote>
                <p><a href="https://en.wikipedia.org/wiki/Reddit" target="_blank" rel="noopener noreferrer">Wikipedia</a>: <span className={styles.quote}>&quot;Reddit is an American social news aggregation, web content rating, and discussion website. Registered members submit content to the site such as links, text posts, images, and videos, which are then voted up or down by other members. Posts are organized by subject into user-created boards called &quot;communities&quot; or &quot;subreddits&quot;, which cover a variety of topics such as news, politics, religion, science, movies, video games, music, books, sports, fitness, cooking, pets, and image-sharing.&quot;</span></p>
            </blockquote>
            <p>And, in Reddit&apos;s own words: <span className={styles.quote}>&quot;At its core, Reddit is a network of communities.&quot;</span></p>
        </div>

        <hr></hr>

        <div className={styles.section}>
            <p>Hi! 🙂 This project is my attempt to automate the process of identifying and sorting subreddits by quality. Overall, I&apos;m pretty happy with the outcome and with the accuracy of the algorithm – it&apos;s not perfect, but it&apos;s more than good enough.</p>
            <p>I created this project mainly because I don&apos;t like what&apos;s <a href="https://www.reddit.com/r/all/" target="_blank" rel="noopener noreferrer">popular on Reddit</a>. It is, in my opinion, nothing but an endless deluge of low-quality content. The kind of content that is easy to create and easier to digest. The kind of content that doesn&apos;t give rise to too much thinking, interaction, or actual communication between the users, but instead lends itself very well to a mindless scrolling and instant gratification. I can understand the appeal, but I don&apos;t think gorging on it is healthy.</p>
            <p>I&apos;m much more curious about what lies beyond Reddit&apos;s frontpage. Is it just more of the same? More meaningless pleasure? Or, are there smaller communities, of higher quality, that don&apos;t show up on the frontpage? Smaller subreddits that are obscured from and not-yet-tainted by the masses, that have managed to preserve some aura of actual community and value. If so, which ones are they? And how many of them are there?</p>
        </div>

        <hr></hr>

        <div className={styles.section}>
            <p>In doing research for this project, I found and was spurred on by others who had also observed this phenomenon of the popular being coupled with a degrading quality. Here are a few:</p>
            <blockquote>
                <p><a href="https://news.ycombinator.com/item?id=27645482" target="_blank" rel="noopener noreferrer">hhjinks</a>: <span className={styles.quote}>&quot;It infuriates me to no end when communities I&apos;ve frequented for years literally get supplanted by faceless non-contributing vagrants who never contribute, comment, or post. They just see funny picture, blow air out their nose, and upvote, not knowing that they&apos;re incentivizing behaviour that&apos;s killing the community that built the space in the first place.&quot;</span></p>
            </blockquote>
            <blockquote>
                <p><a href="https://news.ycombinator.com/item?id=27643533" target="_blank" rel="noopener noreferrer">fullshark</a>: <span className={styles.quote}>&quot;Subreddits get too large and are dominated by lowest common denominator quips and memes to the point that the content is junk food for echo chambers.&quot;</span></p>
            </blockquote>
            <blockquote>
                <p><a href="https://news.ycombinator.com/item?id=27644237" target="_blank" rel="noopener noreferrer">mioasndo</a>: <span className={styles.quote}>&quot;The purpose of reddit at this point is to keep as many naive and docile users as possible, and keep them clicking. Anything that could cause cognitive dissonance is bannable, while advertising and astroturfing are essentially encouraged. Any interesting comment or opinion that&apos;s actually worth reading will be hidden near the bottom or middle of any popular thread. If you try to engage in any potentially controversial conversation, you are at risk of getting banned, or having several comments in the convo deleted. The only thing left worth anything in on reddit are relatively small, niche subreddits.&quot;</span></p>
            </blockquote>
            <blockquote>
                <p><a href="https://news.ycombinator.com/item?id=27644602" target="_blank" rel="noopener noreferrer">steelframe</a>: <span className={styles.quote}>&quot;I once spent an entire weekend collecting and aggregating data to create a bunch of charts that revealed some really interesting statistics for a subreddit and earned about 100 karma. I made a one-line &quot;zinger&quot; comment on some random thread in r/pics and pulled in 1,800 karma. That&apos;s when I realized I was casting pearl before swine by spending real effort on Reddit, and I should instead be directing my efforts on real quality content elsewhere.&quot;</span></p>
            </blockquote>
            <p>Also: <a href="https://knowingless.com/2017/05/02/internet-communities-otters-vs-possums/" target="_blank" rel="noopener noreferrer">Internet communities: Otters vs. Possums</a></p>
            <p>And: <a href="https://news.ycombinator.com/item?id=31363153" target="_blank" rel="noopener noreferrer">Is it true that any community that grows big enough, gets ruined?</a></p>
        </div>

        <hr></hr>

        <div className={styles.section}>
            <p>I started out believing that in order to determine the quality of a subreddit I would have to look at, and include, as much subreddit data as I could get my hands on. Everything from the characteristics of the post titles to analyzing the history of the subreddit&apos;s moderators. Because more is better, right?</p>
            <p>It, however, turns out that I was wrong. There&apos;s really no need to look at all of the data available. The most reliable indicator of a subreddit&apos;s quality is not found in the content itself or in a bunch of auxiliary data, but instead it&apos;s found by looking at the <em>responses</em> to the content. Do the users respond to the content? And <em>how</em> do they respond to the content?</p>
            <p>There seems to be a strong correlation between the quality of the comments and the overall quality of the subreddit. I was only able to understand this after spending a lot of time getting close to and examining the data from different angles. So the answer, it turns out, was simple. But finding it, and then refining it, was not.</p>
        </div>

        <hr></hr>

        <div className={styles.section}>
            <p>Thanks to Reddit for their <a href="https://www.reddit.com/dev/api/" target="_blank" rel="noopener noreferrer">API</a>.</p>
            <p>Thanks to <a href="https://frontpagemetrics.com/list-all-subreddits" target="_blank" rel="noopener noreferrer">frontpagemetrics</a> for sharing metadata (name, description, created_date, subs) of all subreddits.</p>
            <p>By the way, not all subreddits were analyzed. Only those with at least 10,000 subscribers were. The main reason for this is that there are, in total, a bit over <em>three million</em> subreddits and there&apos;s no freaking way that I&apos;m wasting resources (whether mine or Reddit&apos;s) requesting data of more than three million subreddits. Narrowing the scope is the only thing that made sense.</p>
        </div>
    </div>
}