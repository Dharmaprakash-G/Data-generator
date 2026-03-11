import React from 'react'

interface ContainerProps {
    children: React.ReactNode;
}

function Container({ children }: ContainerProps) {
    return (
        <div className='w-full min-h-screen bg-gray-50 p-10'>
            <div className=' mx-auto bg-white shadow-md rounded-xl p-10'>
                {children}
            </div>
        </div>
    )
}

export default Container