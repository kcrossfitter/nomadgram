import React from 'react'
import PropTypes from 'prop-types'

import styles from './styles.scss'
import Loading from 'components/Loading'

const LoadingFeed = (props) => (
  <div className={styles.feed}>
    <Loading />
  </div>
)

const Feed = (props) => {
  if (props.loading) {
    return <LoadingFeed />
  }
}

Feed.propTypes = {
  loading: PropTypes.bool.isRequired
}

export default Feed

