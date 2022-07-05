import Link from 'next/link'
import { useRouter } from 'next/router';
import styles from '../styles/navbar.module.css'
import miscStyles from '../styles/misc.module.css'

export default function Navbar() {
    return <div className={styles.navbar}>
        <h1>dd-subreddits</h1>
        <div>
            <NavItem href="/" text="Home" /> - <NavItem href="/what" text="What?" />
        </div>
    </div>
}

function NavItem({ href, text }) {
    const router = useRouter();
    const isActive = router.asPath === href;
    return (
        <Link href={href}>
            <a className={isActive ? miscStyles['bold-weight'] : miscStyles['normal-weight']}>{text}</a>
        </Link>
    );
}