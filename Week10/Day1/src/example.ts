type Users = {
  id: number;
  password: number | string;
  email: string;
  createdAt: Date;
  updatedAt: Date;
};

// This is how another type object can inherit the one we just made.
type MasterUsers = Users & {
  clearanceLevel: "Top Secret" | "Basic";
};

const ourUsers: MasterUsers[] | Users[] = [];
