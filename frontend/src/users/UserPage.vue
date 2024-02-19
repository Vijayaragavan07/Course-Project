<template>
    <div class="m-3 flex flex-row items-center justify-center">
        <Card title="Welcome User!" class="w-full max-w-md mt-4">
          <form class="flex flex-col space-y-2 w-full">
            <Input
              required
              name="email"
              type="text"
              placeholder="example@email.com"
              label="User ID"
            />
            <Input
              required
              name="password"
              type="password"
              placeholder="••••••"
              label="Password"
            />
            <Button variant="solid"
              >Login</Button
            >
          </form>
        </Card>
      </div>
    
</template>