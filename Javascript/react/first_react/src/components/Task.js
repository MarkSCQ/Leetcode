import { FaTimes } from 'react-icons'

const Task = ({ task }) => {
    return (
        <div className='task'>
            <h3>{task.id}</h3>
            <h3>{task.id}</h3>
            <h3>{task.text}</h3>
        </div>
    )
}

export default Task