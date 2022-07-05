import { getFirestore, collection, getDocs, startAfter, query, orderBy, limit } from 'firebase/firestore/lite';
import firebaseApp from '../lib/firestore_app'
import { useState, useEffect } from 'react';
import styles from '../styles/subreddits.module.css'

export default function SubredditsModule() {
    const [subredditsList, setSubredditsList] = useState([]);
    const [lastVisible, setLastVisible] = useState(null)
    const db = getFirestore(firebaseApp);

    useEffect(() => { getSubreddits() }, []);

    async function getSubreddits() {
        const query = getQuery(db, lastVisible)
        const querySnapshot = await getDocs(query);
        const subreddits = querySnapshot.docs.map(doc => doc.data());
        setSubredditsList(subredditsList.concat(subreddits));
        setLastVisible(querySnapshot.docs[querySnapshot.docs.length - 1])
    }

    return <div className={styles.subredditsModule}>
        <header>
            <strong>Subreddit Name</strong>
            <strong>Subscribers</strong>
        </header>

        <div>
            {subredditsList.map(subreddit =>
                <div key={subreddit.name} className={styles.subredditCard}>
                    <div>
                        <div className={styles.subredditName}>
                            <a href={`https://old.reddit.com/r/${subreddit.name}/top/?sort=top&t=month`} target="_blank" rel="noopener noreferrer">{subreddit.name}</a>
                        </div>
                        <div className={styles.subredditDescription}>{subreddit.desc}</div>
                    </div>
                    <div className={styles.subredditSubscribers}>{subreddit.numSubscribers.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}</div>
                </div>)}
        </div>

        <div className={styles.showSubreddits}>
            <button type="button" onClick={getSubreddits}>Load more</button>
            <span>{`(showing 1-${subredditsList.length} of 2765)`}</span>
        </div>

    </div>
}


function getQuery(db, lastVisible) {
    const initialQuery = query(collection(db, "subreddits"), orderBy("commentsMedian", "desc"), limit(5));

    const nextQuery = query(collection(db, "subreddits"), orderBy("commentsMedian", "desc"), startAfter(lastVisible), limit(5));

    return lastVisible ? nextQuery : initialQuery;
}